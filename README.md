# 🖥️  Studynotes


   A note-taking app using Youtube Data API to retrieve data, so you can watch your tutorial or course while taking your notes with a powerful text editor.

---

![search](https://user-images.githubusercontent.com/66017329/179422281-54ed81d2-7ed8-4f32-a8e0-dce719d803a8.PNG)

![layout](https://user-images.githubusercontent.com/66017329/179422284-24092a78-f30c-4917-8b2f-35fe2f7d3f61.PNG)

![notes](https://user-images.githubusercontent.com/66017329/179422291-00b416c4-5f4c-46cb-ade1-49b0bd682340.PNG)

## How to run Studynotes

1. Generate a [Youtube API KEY](https://www.embedplus.com/how-to-create-a-youtube-api-key.aspx) 

2. When you open **studynotes/setting.py** you'll see in the last line :
```
   
YOUTUBE_API = 'ytbAPi' 
```

- After getting your API KEY, replace your API KEY :

``YOUTUBE_API = "YOUR API KEY HERE"``

Then save the file.

3. Now just open up your terminal and run these commands :

```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

 And there you have it, your note-taking website ! 

