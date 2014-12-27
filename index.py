#!/usr/bin/env python
import sys, re, operator, string


def file_to_lines(path):
	with open(path) as f:
		data = f.readlines()
	return data

def filter_chars(str_data):
	pattern = re.compile('[\W_]+')
	return pattern.sub(' ', str_data)

def normalize(str_data):
	return str_data.lower()

def scan(str):
	return str.split()

def remove_stop_words(word_list):
	global stop_words
	return [w for w in word_list if not w in stop_words]

with open('stop_words.txt') as f:
	stop_words = f.read().split(',')
stop_words.extend(list(string.ascii_lowercase))

page_num = 1
line_num = 1
word_dict = {}
for l in file_to_lines(sys.argv[1]):
	words = remove_stop_words(scan(normalize(filter_chars(l))))
	pattern = re.compile('[0-9]+')
	words = [w for w in words if not pattern.match(w)]
	for w in words:
		if w not in word_dict:
			word_dict[w] = []
		pages = word_dict[w]
		if page_num not in pages:
			pages.append(page_num)
	line_num += 1
	if (line_num%45 == 0):
		page_num += 1

items = sorted(word_dict.iteritems(), key=operator.itemgetter(0)) 

for (w, pages) in items:
	if len(pages) < 100:
		print w, pages
