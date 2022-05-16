def transform_to_row(infile, outfile):

    with open(infile, "r", encoding = "utf-8") as reader:
         contents = reader.readline()
         text = contents.split(",")
    with open(outfile, "w", encoding = "utf-8") as writer:
         for items in text:

            writer.write(items+'\n')


transform_to_row("/Users/irynamalashenko/Downloads/names_inline.txt", "/Users/irynamalashenko/Downloads/lines.txt")

def add_greeting(infile, outfile):
    phrase = "Hello "
    with open(infile, "r", encoding="utf-8") as reader:
        lines = reader.readlines()
    with open(outfile, "w", encoding="utf-8") as writer:
        for item in lines:
            writer.write(phrase+item)

add_greeting("/Users/irynamalashenko/Downloads/lines.txt","/Users/irynamalashenko/Downloads/greetings.txt")


def strip_greeting(infile, outfile):
    with open(infile, "r", encoding="utf-8") as reader:
        lines = reader.readlines()
    with open(outfile, "w", encoding="utf-8") as writer:
        for item in lines:
            strip_line = item.strip("Hello ")
            writer.write(strip_line)
strip_greeting("/Users/irynamalashenko/Downloads/lines.txt","/Users/irynamalashenko/Downloads/greetings.txt")

def combine_files(file1, file2, outfile):
    with open(file1, "r") as read_file1:
        
        with open(file2, "r") as read_file2:
            text_file1 = read_file1.readlines()
            text_file2 = read_file2.readlines()
            
            if len(text_file1) != len(text_file2):
                return "Error in line"
                
            with open(outfile, "w") as writer:
                for item in range(len(text_file1)):
                    combine = text_file1[item].strip("\n") + " " + text_file2[item]
                    writer.write(combine)
combine_files("/Users/irynamalashenko/Downloads/lines.txt", "/Users/irynamalashenko/Downloads/file2.txt", "/Users/irynamalashenko/Downloads/file3.txt")



