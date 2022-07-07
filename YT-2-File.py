import pytube as pt
import pandas as pd
import os

path = os.path.join(os.environ["USERPROFILE"], "Videos")
# path = 'D:\Videos'

def download():
    link_search = input('Your YouTube Video/Playlist/Channel/Title: ')

    if 'https://www.youtube.com/watch?' in link_search:
        index_list = []
        yt = pt.YouTube(link_search)
        selection = yt.streams.filter(progressive=True, subtype='mp4').order_by('resolution').last()
        
        file_name = yt.title + '.mp4'

        download_path = selection.download(filename=file_name,output_path = path)
        
        print('')
        print(f'Video downloaded to: "{download_path}"')
        print('')
        
    # elif 'https://www.youtube.com/playlist?' in link_search:
    #     playlist = pt.Playlist(link_search)
        
    #     video_list = playlist.videos
        
    #     for video in video_list:
    #         file_name = video.title + '.mp4'
    #         download_path = video.streams.filter(progressive=True, subtype='mp4').order_by('resolution').last().download(filename=file_name,output_path = path)
    #         print('')
    #         print(f'Audio downloaded to: "{download_path}"')
    #         print('')
        
    elif 'https://www.youtube.com/channel/' in link_search or 'https://www.youtube.com/c/' in link_search:
        channel = pt.Channel(link_search)
        
        video_list = channel.videos
        
        for video in video_list:
            file_name = video.title + '.mp4'
            download_path = video.streams.filter(progressive=True, subtype='mp4').order_by('resolution').last().download(filename=file_name,output_path = path)
            print('')
            print(f'Video downloaded to: "{download_path}"')
            print('')

    else:
        index_list = []
        
        search = pt.Search(link_search)
        dicc = {'Title': [],
                'Author': [],
                'URL': [] 
                }
        
        for index,result in enumerate(search.results):
            rs = vars(result)
            index_list.append(index + 1)
            dicc['Title'].append(rs.get('_title'))
            dicc['Author'].append(rs.get('_author'))
            dicc['URL'].append(rs.get('watch_url'))
                
        df = pd.DataFrame(dicc, index=index_list)
        
        print('')
        print(df)
        print('')
        
        selection = int(input('Please select your video by index: '))
        print('')
        
        yt = pt.YouTube(df['URL'][selection])
        
        selection = yt.streams.filter(progressive=True, subtype='mp4').order_by('resolution').last()
    
        file_name = yt.title + '.mp4'

        download_path = selection.download(filename=file_name,output_path = path)
        
        print('')
        print(f'Video downloaded to: "{download_path}"')
        print('')
    
    download()
    
download()