def cleanText(line):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~|'''
    for x in line.lower(): 
        if x in punctuations: 
            line = line.replace(x, " ") 
    return line
def run(line):
    formatted_line = cleanText(line)
    return formatted_line
if __name__ == "__main__":
    print(run("DAwdawdn, dnd|wdwdnajwdn,dawdmwd"))