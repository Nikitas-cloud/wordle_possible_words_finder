import urllib.request

# Downloads and merges all words (Answers + Allowed Guesses)
def get_full_wordle_dictionary():
    # URL 1: List of official answers
    url_answers = "https://gist.githubusercontent.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b/raw/wordle-answers-alphabetical.txt"
    # URL 2: List of all other allowed guess words
    url_allowed = "https://gist.githubusercontent.com/cfreshman/cdcdf777450c5b5301e439061d29694c/raw/wordle-allowed-guesses.txt"
    
    all_words = set() # Using a set to prevent duplicates
    
    try:
        # Download answers
        resp1 = urllib.request.urlopen(url_answers)
        answers = resp1.read().decode('utf-8').splitlines()
        all_words.update(answers)
        
        # Download allowed words
        resp2 = urllib.request.urlopen(url_allowed)
        allowed = resp2.read().decode('utf-8').splitlines()
        all_words.update(allowed)
        
        return list(all_words)
    except Exception as e:
        print("Error loading dictionary:", e)
        return []

def get_possible_words(dictionary, green_letters, yellow_letters, gray_letters):
    possible_words = []
    
    for word in dictionary:
        is_valid = True
        
        for pos, char in green_letters.items():
            if word[pos] != char:
                is_valid = False
                break
        if not is_valid: continue
            
        for pos, char in yellow_letters:
            if char not in word or word[pos] == char:
                is_valid = False
                break
        if not is_valid: continue
            
        for char in gray_letters:
            if char in word:
                is_valid = False
                break
                
        if is_valid:
            possible_words.append(word)
            
    return sorted(possible_words) # Returns the words in alphabetical order

# --- Interactive Main Program ---
if __name__ == "__main__":
    wordle_dictionary = get_full_wordle_dictionary()
    
    if not wordle_dictionary:
        print("Failed to load the dictionary. Exiting...")
    else:
        print(f"Successfully loaded {len(wordle_dictionary)} words! The program is ready.")
        print("-" * 40)

        # Initialize collections to keep track of hints throughout the game
        current_green = {}
        current_yellow = []
        current_gray = set()

        while True:
            print("\nEnter your new hints (or press Enter if you have nothing new for a category).")
            print("Type 'exit' to quit the program.")
            
            # 1. Green Letters Input
            gr_input = input("GREEN (format 'PositionLetter' e.g., 2o 4e 5l): ").lower().split()
            if 'exit' in gr_input: break
            for item in gr_input:
                pos = int(item[:-1]) - 1 # Convert 1-based to 0-based index
                char = item[-1]
                current_green[pos] = char
                
            # 2. Yellow Letters Input
            yl_input = input("YELLOW (format 'PositionLetter' e.g., 1a 3m): ").lower().split()
            if 'exit' in yl_input: break
            for item in yl_input:
                pos = int(item[:-1]) - 1
                char = item[-1]
                current_yellow.append((pos, char))
                
            # 3. Gray Letters Input
            gy_input = input("GRAY (type them continuously e.g., rtuias): ").lower().strip()
            if 'exit' in gy_input: break
            for char in gy_input:
                current_gray.add(char)
                
            # Calculate and display results
            matches = get_possible_words(wordle_dictionary, current_green, current_yellow, current_gray)
            
            print("\n" + "="*40)
            print(f"Found {len(matches)} possible words:")
            # Display only the first 20 if the list is too long
            if len(matches) > 20:
                print(", ".join(matches[:20]).upper() + f" ... (and {len(matches)-20} more)")
            else:
                print(", ".join(matches).upper())
            print("="*40)