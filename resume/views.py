from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Upload
from django.shortcuts import render

# from pdf2image import convert_from_path
# import easyocr
# import numpy as np
# import PIL
# from PIL import ImageDraw
# import spacy


# def draw_boxes(image, bounds, color='yellow', width=2):
#     draw = ImageDraw.Draw(image)
#     for bound in bounds:
#         p0, p1, p2, p3 = bound[0]
#         draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
#     return image



# draw_boxes(images[0], bounds)

# import os
# nlp = spacy.load("en_core_web_sm")
# doc = nlp(text)
# svg = spacy.displacy.render(doc, style="dep")
# output_path = Path(os.path.join("./", "sentence.svg"))
# output_path.open('w', encoding="utf-8").write(svg)

class UploadView(CreateView):
    model = Upload
    fields = ['upload_file', ]
    success_url = reverse_lazy('fileupload')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Upload.objects.all()
        return context

import os
# from djangoProject.settings import BASE_DIR

# def resume_text(request):
#     reader = easyocr.Reader(['en'])
#     latest_object = Upload.objects.all().order_by('-upload_date')[0]
#     relative_path = "\\media\\" + str(latest_object.upload_file)
#     file_path = str(BASE_DIR) + relative_path
#     images = convert_from_path(file_path)
#     bounds = reader.readtext(np.array(images[0]), min_size=0, slope_ths=0.2, ycenter_ths=0.7, height_ths=0.6,
#                              width_ths=0.8, decoder='beamsearch', beamWidth=10)
#     # text = ''
#     text = []
#     for i in range(len(bounds)):
#         text.append(bounds[i][1])
#         # text = text + bounds[i][1] + '\n'
#     return render(request, 'resume/resume_result_text.html', context={'text': text})
