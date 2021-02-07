### Mongo DB

Notre base de donnée comporte une 'database' : youtube, qui contient elle mêmes 4 collections :

- channels : qui contient des documents concernant les chaînes
- comments : qui contient des documents concernant les commentaires
- playlist :  qui contient des documents concernant les playlist
- videos : qui contient des documents concernant les vidéos

Exemple d'un document channels 
```
> db.channels.findOne({})
{
        "_id" : "UCirPbvoHzD78Lnyll6YYUpg",
        "channel_title" : "buildwithpython",
        "channel_description" : "Learn python by building in-depth projects and going beyond the basics. The channel currently includes Python Network Programming, Socket Programming, ...",
        "img" : "https://yt3.ggpht.com/ytc/AAUvwng7O_0vmJZmhiThH_zHVPJt84WmeiLKJ2bjcIkJ=s88-c-k-c0xffffffff-no-rj-mo",
        "created" : ISODate("2018-06-14T10:24:22Z"),
        "last_update" : ISODate("2021-01-29T14:30:44.038Z")
}
>
```

Exemple d'un document comments 
```
> db.comments.findOne({})
{
        "_id" : "UgwSizFNxypDW_UViC94AaABAg",
        "video_id" : "7cIBAh1iuAw",
        "author_name" : "YouTube Lovers",
        "text" : "You are legand programmer 🐢🐢🐢",
        "author_profile_picture" : "https://yt3.ggpht.com/ytc/AAUvwngxYp8IE2eRvGsTW4K3nIqBxHb19Z7hG14nwSlD=s48-c-k-c0xffffffff-no-rj-mo",
        "author_id" : "UCPL_kEEdKGc-3eUfznAEd9A",
        "likes" : 1,
        "date_published" : ISODate("2020-09-24T05:51:33Z"),
        "date_updated" : ISODate("2020-09-24T05:51:33Z"),
        "replies" : 1
}
>

```
Exemple d'un document videos
```
> db.videos.findOne({})
{
        "_id" : "7cIBAh1iuAw",
        "id_playlist" : "PLhTjy8cBISEqaIHMiJr8gNsH37R4ks69m",
        "dislikes" : 1,
        "likes" : 42,
        "post_date" : ISODate("2020-09-23T00:00:00Z"),
        "titre" : "Python Django Tutorial - #4 - Lessons Model and URL slug",
        "vues" : 759
}
>
```
Exemple d'un document playlist
```
> db.playlist.findOne({})
{
        "_id" : "PLhTjy8cBISEqaIHMiJr8gNsH37R4ks69m",
        "id_youtubeur" : "UCirPbvoHzD78Lnyll6YYUpg",
        "playlist" : "Python Django Tutorial - Building a Startup | Livestream",
        "nbr_videos" : "15",
        "derniere_maj" : "Oct 20, 2020",
        "vues" : "1859 ",
        "url_img" : "https://i.ytimg.com/vi/DlMqqtUkb8o/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBEcU3wUcIVfddpmbXeZw_8AIgvFg",
        "description" : "",
        "video_time" : [
                "1:35:30",
                "1:42:50",
                "1:28:36",
                "1:35:58",
                "1:19:22",
                "1:43:20",
                "1:34:40",
                "37:37",
                "1:57:30",
                "1:14:16",
                "1:39:55",
                "1:35:43",
                "1:48:40",
                "1:33:07",
                "1:22:00"
        ]
}
>
```



