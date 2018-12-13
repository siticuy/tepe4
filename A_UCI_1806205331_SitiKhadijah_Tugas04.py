from PIL import Image
import os

def resize(x,y,filename):
    file,ext = os.path.splitext(filename)
    size = x,y
    im = Image.open(filename)
    new_im=im.resize(size)
    new_im.save(f'{file}_{size}{ext}')
    im.close()

def change_ext(filename):
    file,ext = os.path.splitext(filename)
    if ext.lower() == '.jpg':
        im = Image.open(filename)
        im.save(f'{file}_new_ext.png')
        im.close()
    else:
        im = Image.open(filename)
        im.save(f'{file}_new_ext.jpg')
        im.close()
def rotate(angle,filename):
    im = Image.open(filename)
    im_rotate = im.rotate(angle, expand='True',fillcolor='white')
    im_rotate.save(f'{filename}_rotate.jpg')
    im.close()

def main():
    os.chdir('C:/Users/USER/Pictures/tp4/')
    print('------------------------------------------\n'
          '---Welcome to simple image edit program---\n'
          '------------------------------------------\n')
    print('the image file only in .jpg or .png')
    filename = input('Input your image name[cat1.jpg]: ')
    
    if os.path.exists(filename)==False:
        print(f'Your find is not exist in C:/Users/USER/Pictures/tp4/\n'
              'Please check your folder\n')
    else:
        if filename[-4:].lower()=='.jpg' or filename[-4:].lower()=='.png':
            file, ext = os.path.splitext(filename)
            menu = print('1. Resize image \n'
                       '2. Change image ext \n'
                       '3. Rotate image')
            choose = input('What do you choose? ')
            if choose == '1':
                inp_size_x = int(input('Input size in pixel, x: '))
                inp_size_y = int(input('Input size in pixel, y: '))
                resize(inp_size_x,inp_size_y,filename)
                print('Check your folder to see the resized image')
             
            elif choose == '2':
                menu_ext = print('Choose ext you want :\n'
                               '1. .jpg\n'
                               '2. .png\n')
                choose_ext = input('Choose either 1 or 2: ')
                if choose_ext == '1' or choose_ext == '2':
                    change_ext(filename)
                    print('Check your folder to see the new ext image')
                else:
                    print('Choose only either 1 or 2')
                
            elif choose == '3':
                inp_angle = int(input('Input angkle to rotate image[ex=90]: '))
                rotate(inp_angle,filename)
                print('Check your folder to see the rotated image')
            else:
                  print('Choose only either 1,2, or 3')
        else:
              print('Your extension must be .png or .jpg')

if __name__=='__main__':
    main()


