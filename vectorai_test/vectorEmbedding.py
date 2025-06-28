import logging
from openai import OpenAI
from database import createDbEntry
from data_class import Movie
from constant import openai_api_key
from data_transfer_object import MovieRequest

def generate_embedding(input,model):
    try:
        error =""
        client = OpenAI(api_key=openai_api_key)
        response = client.embeddings.create(
            input=input,
            model=model
        )
        if hasattr(response, 'status_code') and response.status_code != 200:
            logging.error(f"Bad status code: {response.status_code}")
            return "", f"Request failed with status code {response.status_code}"

        return response, ""
    except Exception as e:
        logging.info("Exception occurred while generating embedding")
        error = str(e)
        return "", error


def process_request(movie_data):
    try:

        model = "text-embedding-3-small"
        embedding,error = generate_embedding(movie_data.description,model)

        if error :
            return error

        if embedding :
            movie = Movie(movie_data.title,embedding)
            err, msg = createDbEntry("movies", movie)
            if err:
                return  "",err

            return msg,""

        return "Unknown error: No embedding and no error returned."
    except Exception as e:
        logging.exception("Exception occurred in process_request")
        err = "Exception"
        return f"Exception: {str(e)}"



if __name__ == '__main__':
    test_movie = MovieRequest("Inception", "A mind-bending thriller where dreams are real.")
    print(process_request(test_movie))
    pass






