from io import BytesIO
from PIL import Image

layout_mapping = {
    'PICTURE_SLIDE' : 8,
    'TITLE' : 0,
}


def add_title_slide(presentation, slide_title, slide_subtitle):
    title_slide_layout = presentation.slide_layouts[layout_mapping['TITLE']]
    slide = presentation.slides.add_slide(title_slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    title.text = slide_title
    subtitle.text = slide_subtitle
def add_picture_slide(presentation, image, slide_title, subtext="", resize_or_crop = False):
    '''

    :param presentation:
    :param image: Can be file name or bytes like object
    :param slide_title:
    :param subtext:
    :return:
    '''
    layout = presentation.slide_layouts[layout_mapping['PICTURE_SLIDE']]
    slide = presentation.slides.add_slide(layout)

    title = slide.shapes.title
    title.text = slide_title
    if subtext:
        subtitle = slide.placeholders[2]
        subtitle.text = subtext

    placeholder = slide.placeholders[1]



    if type(image) == str:
        mimg = Image.open(image)
        image_stream = BytesIO()
        mimg.save(image_stream, 'png')

    elif type(image) == BytesIO: #bytes stream
        mimg = Image.open(image)
        image_stream = image
    else:
        print("Warning! Not image or file name provided... Try to see if matplot figure")
        image_stream = BytesIO()
        image.savefig(image_stream)
        mimg = Image.open(image_stream)

    if not resize_or_crop:
        placeholder.width = mimg.width
        placeholder.height = mimg.height

    placeholder.insert_picture(image_stream)
    image_stream.close()

    pass