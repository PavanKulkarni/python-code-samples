def build_anagram_dict(input):
    input_list = input.split()
    character_frequency_dict = {}
    for (idx, word) in enumerate(input_list):
    	for character in word:
    		if character not in character_frequency_dict:
    			character_frequency_dict[character] = []
    		character_frequency_dict[character].append(idx)
    print character_frequency_dict

if __name__ == '__main__':
    input_string = 'test hello facebook google madam tree height width laptop palantir dropbox uber linkedin'
    build_anagram_dict(input_string)