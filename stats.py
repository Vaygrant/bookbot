def count_number_of_words(text):
    return len(text.split())

def inventory_all_characters(text):
    return_dictionary = {}
    for character in text:
        if character.lower() not in return_dictionary.keys():
            return_dictionary[character.lower()] = 0
        
        return_dictionary[character.lower()] += 1
    
    return sort_dictionary(return_dictionary)

def sort_dictionary(dictionary):
    return_dictionary = {}

    for entry in dictionary:
        if entry.isalpha():
            return_dictionary[entry] = dictionary[entry]
    
    return {k: v for k, v in sorted(return_dictionary.items(), key=lambda item: item[1], reverse=True)}