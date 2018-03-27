from extract import get_genre
import sys, getopt
import glob

def main():
	path = './'
	fileExt = '.mp3'

	if len(sys.argv) >= 2:
		try:
			opts, args = getopt.getopt(sys.argv[1:], "e:h", ["help", "extension"])
		except getopt.GetoptError as err:
			print(err)
			sys.exit(2)

		if sys.argv[1] not in [arg[0] for arg in opts]:
			path = sys.argv[1]
			if path[-1] != '/':
				path += '/'

		for opt, arg in opts:
			if opt in ("-h", "--help"):
				usage()
				sys.exit()

			elif opt in ("-e", "--extension"):
				fileExt = arg

			else:
				assert False, "Unhandled option"

	print_genres(path, fileExt)

def usage():
	print("File genre counter")
	print("Usage: python print_genres [filePath] [-e extension]")
	print("Usage: python print_genres [-e extension]")
	print("--help, -h                  Print this help text")
	print("--extension, -e             File extension")

def print_genres(path, fileExt):
	fileGenres = {}
	for filename in glob.glob(path + '*' + fileExt):
		genre = get_genre(filename)
		
		if not genre in fileGenres:
			fileGenres.update({genre: 0})

		fileGenres[genre] += 1

	for key in fileGenres:
		print('{}: {}'.format(key, fileGenres[key]))

if __name__ == "__main__":
	main()
