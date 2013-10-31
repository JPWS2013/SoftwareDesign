import urllib
import string 

def clean_line(fileline):
    fileline=fileline.replace('-', ' ')
    temp_wordlist=fileline.split(' ')
    out_temp_wordlist=[]
    
    for i in range(len(temp_wordlist)):

        if temp_wordlist[i]=='':
            continue
        else:
            holder=temp_wordlist[i]

            holder=holder.strip(string.whitespace)
            holder=holder.strip('\xef\xbb\xbf')
            holder=holder.strip(string.punctuation)
            holder=holder.lower()

            out_temp_wordlist.append(holder)

    return out_temp_wordlist

def town_extract():
    findTown=False

    for line in open('urlcontents.txt'):
        holder=clean_line(line)

        if findTown==True:
            town_wordList=line.split(',')
            town=town_wordList[0][19:]
            return town

        if 'is' and 'the' and 'zip' and 'code' and 'for</h3'in holder:
            findTown=True

def population_extract():

    for line in open('urlcontents.txt'):
        holder=clean_line(line)

        for eachString in holder:
            if eachString[:10]=='population':
                populationstring=eachString
                popMag=populationstring[19:-5]
                return popMag



if __name__ == '__main__':
    zipCode=raw_input("Please enter a US Zip Code: ")

    finalurl="http://www.uszip.com/zip/"+zipCode

    page=urllib.urlretrieve(finalurl, 'urlcontents.txt')

    town=town_extract()

    population=population_extract()

    print "You have entered the zipcode for the town of ", town, " which has a population of ", population