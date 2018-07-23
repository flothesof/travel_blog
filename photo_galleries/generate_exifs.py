import os
import piexif

if __name__ == '__main__':
	root, dirs, files = next(os.walk('.'))
	print("Directories found: {}".format(dirs))
	for directory in dirs:
		fnames = os.listdir(directory)
		fnames = [fname for fname in fnames if fname.lower().endswith('jpg') or fname.lower().endswith('jpeg')]
		with open(os.path.join(directory, 'exif.txt'), 'w') as f:
			for fname in fnames:
				try:
					exif_dict = piexif.load(os.path.join(directory, fname))
					camera = exif_dict['0th'][piexif.ImageIFD.Model].decode('utf-8')
					focal_length_tup = exif_dict['Exif'][piexif.ExifIFD.FocalLength]
					focal_length = focal_length_tup[0] / focal_length_tup[1]
					iso = exif_dict['Exif'][piexif.ExifIFD.ISOSpeedRatings]
					fnumber_tup = exif_dict['Exif'][piexif.ExifIFD.FNumber]
					fnumber = fnumber_tup[0] / fnumber_tup[1]
					exposure_time_tup = exif_dict['Exif'][piexif.ExifIFD.ExposureTime]
					exposure_time = "{}/{}".format(*exposure_time_tup)
					f.write("{}: {} - {:.1f} mm F/{:.1f} {} s ISO {}\n".format(fname, camera, focal_length, fnumber, exposure_time, iso))
				except KeyError:
					print('WARNING: could not find exif information for picture {}'.format(fname))