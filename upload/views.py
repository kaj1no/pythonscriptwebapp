from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.contrib import messages
from .models import myuploadfile
from django.http import HttpResponseRedirect
import os
import mimetypes
from django.core.files import File
import time
from datetime import datetime
import shutil 
def run(request):
    return(render(request,'home.html'))

def fileup(request):
    
    if request.method =='POST':
        BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filename='test.txt'
        filepath =BASE_DIR+'/media/'+filename
        if os.path.isfile(filepath):
            os.remove(filepath)
        else:
            myfiles=request.FILES.getlist('myfiles')
            if len(myfiles)==1:
                s=list(map(str,myfiles))
                if s[0]=='test.txt' :
                    for fil in myfiles:
                            my_uploadedfiles=myuploadfile(myfiles=fil)
                            my_uploadedfiles.save()
                    messages.info(request,'Files Uploaded')
                    return HttpResponseRedirect('/')
                else:
                    messages.info(request,'Wrong file')
                    return HttpResponseRedirect('/')
            elif len(myfiles)>2:
                messages.info(request,'More then two file')
                return HttpResponseRedirect('/')
            else:
                messages.info(request,'No File')
                return HttpResponseRedirect('/')
def script(request):
    '''Add your script here and give it file path 
    eg :BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filename='test.txt'
        filepath =BASE_DIR+'/media/'+filename
        s=pd.read_excel(filepath)
    followed by the script
    '''
    time.sleep(10)
    messages.info(request,'Script is successful')
    return HttpResponseRedirect('/')

def downl(request):
    try:
        BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filename='test.txt'
        filepath =BASE_DIR+'/media/'+filename
        path=open(filepath,'rb')
        mime_type,_=mimetypes.guess_type(filepath)
        response=HttpResponse(path,content_type=mime_type)
        response['Content-Disposition']="attachment;filename=%s"%filename
        os.remove(filepath)
        return response
    except FileNotFoundError:
        messages.info(request,'No file to download')
        return HttpResponseRedirect('/')
