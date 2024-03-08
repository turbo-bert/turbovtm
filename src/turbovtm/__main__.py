import turbodinwriter as tw
import json
import subprocess


pdf = tw.DINA4L()

framerate = 25 # per second

slides = json.loads(open("slides.js", "r").read())
image_linker = {}

current_frame = 0

slide_no = 0
for slide in slides:
    slide_no = slide_no+1
    pdf.page(slide_no).text(2, 10, slide["header"])
    pdf.page(slide_no).text(50, 10, slide["footer"])
    fc = slide["seconds"]
    #for f in fc:
    #TODOimage_linker["slide-%d" % slide_no] = [ "slide-%d.jpg " ]


slide_count = slide_no

pdf.build('build/o.pdf')

# convert pages to high-res jpegs
for i in range(0, slide_count):
    cmd = """/bin/bash -c "cd build && convert -density 200 o.pdf[%d] -quality 80 slide-%d.jpg" """ % (i, i+1)
    print(cmd)
    subprocess.check_output(cmd, shell=True, universal_newlines=True)
