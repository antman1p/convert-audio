import os
import sys
import argparse
from pydub import AudioSegment

parser = argparse.ArgumentParser(description='Convert a dir of FLAC files to WAV files')
parser.add_argument('--input_path', type=str, required=True, help='Path to the input .flac files')
parser.add_argument('--output_dir', type=str, required=True, help='Output directory for the .wav files')
parser.add_argument('--from_file', type=str, required=True, help='Output directory for the .wav files')
parser.add_argument('--to_file', type=str, required=True, help='Output directory for the .wav files')

args = parser.parse_args()

input_path = args.input_path
output_dir = args.output_dir
from_type = args.from_file
to_type = args.to_file
outputpath_and_name = ""

# Create output dir if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

#convert
for filename in os.listdir(input_path):
    path_and_name = input_path + filename
    print(path_and_name)
    outputpath_and_name = output_dir + filename
    tmp_audio_data = AudioSegment.from_file(path_and_name, format=from_type)
    tmp_audio_data.export(outputpath_and_name, format=to_type)
    outputpath_and_name = ""
    
# Rename with new file extension
for fn in os.listdir(output_dir):
    infilename = os.path.join(output_dir,fn)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(fn)
    newname = infilename.replace(from_type, to_type)
    output = os.rename(infilename, newname)


#!python convert_audio.py --input_path "./uploads/" --output_dir "./uploads/" --from_file "mp3" --to_file "wav"
