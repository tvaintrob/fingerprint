#!/usr/bin/env python

from pythonopensubtitles.opensubtitles import OpenSubtitles
from pythonopensubtitles.utils import File
import tmdbsimple as tmdb

kind_map = {
    "movie_results": 'movie',
    "tv_episode_results": 'episode'
}


def get_imdb_id(os_user, os_pass, file_path):
    """Used to find IMDB id of a video file, using opensubtitles' hash search

    Args:
        os_user (str): OpenSubtitles username to use.
        os_password (str): OpenSubtitles password to use.
        file_path (str): Path to the video file to use.

    Returns:
        str: IMDB id of the given file.
    """
    os = OpenSubtitles()
    os_token = os.login(os_user, os_pass)
    os_file = File(file_path)
    os_data = os.search_subtitles([{
        'sublanguageid': 'all',
        'moviehash': os_file.get_hash(),
        'moviebytesize': os_file.size
    }])

    return os_data[0].get('IDMovieImdb')


def get_details(os_user, os_pass, tmdb_key, file_path):
    """Used to retrieve details from IMDB given movie id

    Args:
        os_user (str): OpenSubtitles username to use.
        os_password (str): OpenSubtitles password to use.
        tmdb_key (str): themoviedb api key to use
        file_path (str): Path to the video file to use.

    Returns:
        dict: a dictionary containing details on the video file
    """
    tmdb.API_KEY = tmdb_key

    imdb_id = get_imdb_id(os_user, os_pass, file_path)
    tmdb_object = tmdb.Find('tt' + imdb_id).info(external_source='imdb_id')
    tmdb_object = {k: v for k, v in tmdb_object.iteritems() if v != []}.values()[0][0]

    show_details = tmdb.TV(tmdb_object['show_id']).info()
    episode_details = tmdb.TV_Episodes(tmdb_object['show_id'],
                                       tmdb_object['season_number'],
                                       tmdb_object['episode_number']).info()

    return {
        'imdb_id': imdb_id,
        'season': tmdb_object['season_number'],
        'episode': tmdb_object['episode_number'],
        'title': episode_details['name'],
        'series_title': show_details['name']
    }
