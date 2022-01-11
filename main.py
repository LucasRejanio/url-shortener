from modules.shortner import Shortener

def main():
    big_url = input('Please, write the big url: ')
    shortened_url = Shortener(big_url)
    print(shortened_url)

main()
