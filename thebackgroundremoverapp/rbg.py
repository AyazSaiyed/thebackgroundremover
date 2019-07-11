from removebg import RemoveBg
# import argparse
import sys
# program_name = sys.argv[0]

# ap = argparse.ArgumentParser(description="Add Image in Argument")

# ap.add_argument('-i','image',required=True,help="add image in the argument")

# args = vars(ap.parse_args())

rmbg = RemoveBg("jvcu8BVqELyUYURc99sfQbAb", "error.log")
# myimg = args["--image"]

rmbg.remove_background_from_img_file(sys.argv[1])


