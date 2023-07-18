from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'Name': 'Ayus Bhattacharya',
        'Author_Img': 'C:/Users/Ayus/ayusbhatta0702.github.io/Django/Mahimail/photos/My potrait.jpg',
        'Title': 'Blog post 1',
        'Date': '1st January, 2023',
        'Content': 'Lorem Ipsum'
    },
    {
        'Name': 'Mahendra Bahubali',
        'Author_Img': 'https://www.google.com/search?q=mahendra+bahubali&tbm=isch&ved=2ahUKEwic1c-X_5eAAxWwxKACHbzkB-UQ2-cCegQIABAA&oq=mahendra+bahubali&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BAgjECc6CQgAEBgQgAQQCjoHCCMQ6gIQJzoLCAAQgAQQsQMQgwE6CAgAEIAEELEDOgcIABCKBRBDUOAEWIE4YN45aAJwAHgFgAGnBYgBlkuSAQswLjEuNy45LjUuNJgBAKABAaoBC2d3cy13aXotaW1nsAEKwAEB&sclient=img&ei=I2K2ZNy3BbCJg8UPvMmfqA4&bih=657&biw=1366&rlz=1C1SQJL_enIN916IN916#imgrc=NHNvnqmFYLqT0M',
        'Title': 'Blog Post 2',
        'Date': '2nd January, 2023',
        'Content': 'Dipsum Po'
    }
]


# Create your views here.
def home(request):
    context = {
        'posts': posts
        }
    
    return render(request, 'Mahimail/home.html', context)

def about(request):
    context = {
        'title': 'About Us'
    }
    return render(request, 'Mahimail/about.html', context)