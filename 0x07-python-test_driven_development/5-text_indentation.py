#!/usr/bin/python3
def text_indentation(text):
    """
        prints new line twice after . ? :

        Args:
            @text: string of text with the characters specified

        Raises:
            TypeError: text has to be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sentence = []
    text2 = text.lstrip()

    for word in text2:
        if word not in ['.', '?', ':'] or \
            any(x not in ['.', '?', ':'] for x in word):
            sentence.append(word)
    
    print(f"{''.join(str(x) for x in sentence)}")
    print("\n")
