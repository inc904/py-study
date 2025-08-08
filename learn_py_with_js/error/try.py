try:
    with open('file-not-exist.txt', 'r') as f:
        content = f.read()
        lines = content.split('\n')

        for line in lines:
            if line.strip() != '':
                print(line)
        first_line = lines[0].strip()
        print(f'First line: {first_line}')

        numbers = [int(line) for line in lines]
        print(f'Sum of numbers: {numbers}')

except Exception as error:
    print(f'An error occurred: {str(error)}')
