from django.http import HttpResponse
import hashlib
import json
import os
import uuid
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import UploadedFile
from illumina_app.illuminaAI.rag_core import rag_core

def something(request):
    return HttpResponse("Suppp")


def home(request):
    return render(request, "home.html")

def chat_app(request):
    file_id = request.session.get('file_id')
    file_info = None
    
    if file_id:
        try:
            file_obj = UploadedFile.objects.get(id=file_id)
            file_info = {
                'filename': file_obj.original_filename,
                'filepath': file_obj.file_path
            }
        except UploadedFile.DoesNotExist:
            pass
    
    return render(request, "main.html", {'file_info': file_info})

@csrf_exempt
@require_POST
def chat_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")
        file_id = request.session.get('file_id')
        file_path = None
        
        if file_id:
            try:
                file_obj = UploadedFile.objects.get(id=file_id)
                file_path = file_obj.file_path
                db_name = f"db_{file_obj.unique_filename.split('.')[0]}"
                try:
                    reply = rag_core(file_path, db_name, user_message)
                except Exception as e:
                    reply = f"Error processing your request: {str(e)}"
            except UploadedFile.DoesNotExist:
                reply = "Error: The file you uploaded is no longer available."
        else:
            reply = "Please upload a file first to chat with the assistant."

        return JsonResponse({"reply": reply})
    return JsonResponse({"error": "Invalid request"}, status=400)


def calculate_file_hash(uploaded_file):
    """Calculate SHA-256 hash of uploaded file."""
    sha256 = hashlib.sha256()
    for chunk in uploaded_file.chunks():
        sha256.update(chunk)
    uploaded_file.seek(0)
    return sha256.hexdigest()

def file_upload(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        file_hash = calculate_file_hash(uploaded_file)
        existing_file = UploadedFile.objects.filter(file_hash=file_hash).first()
        
        if existing_file:
            request.session['file_id'] = existing_file.id
            return redirect('chat_app')
        
        unique_filename = str(uuid.uuid4())
        file_extension = os.path.splitext(uploaded_file.name)[1]
        new_filename = unique_filename + file_extension
        
        upload_folder = os.path.join(settings.BASE_DIR, 'illumina', 'uploads')
        os.makedirs(upload_folder, exist_ok=True)
        
        file_path = os.path.join(upload_folder, new_filename)
        
        try:
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            
            file_obj = UploadedFile.objects.create(
                original_filename=uploaded_file.name,
                unique_filename=new_filename,
                file_hash=file_hash,
                file_path=file_path
            )
            
            request.session['file_id'] = file_obj.id
            return redirect('chat_app')
            
        except Exception as e:
            return render(request, 'file_upload.html', {
                'error_message': f'Error uploading file: {e}'
            })
    
    return render(request, 'file_upload.html')

def get_file_path_by_id(file_id):
    try:
        file_obj = UploadedFile.objects.get(id=file_id)
        return file_obj.file_path
    except UploadedFile.DoesNotExist:
        return None

