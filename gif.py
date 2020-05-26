import imageio
import os

clip = os.path.abspath('k.mp4')

def gif_maker(inputPath,targetFormath):
    outputPath = os.path.splitext(inputPath)[0] + targetFormath

    print(f'converting{inputPath} \n to {outputPath}')

    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outputPath,fps=fps)

    for frame in reader:
        writer.append_data(frame)
        print(f'Frame{frame}')
    print("Done")
    writer.close()

gif_maker(clip,'.gif')        