import requests

from concurrent.futures import ThreadPoolExecutor, wait

from settings import (
    GOOGLE_API_KEY,
    GOOGLE_CUSTOM_SEARCH_URI,
    SEARCH_ENGINE_ID,
    db
)


def search(search_text, user_id):
    """Fetches results from google custom search API
    Stores searched text in parallel using threadpool.

    Args:
        search_text: Search text provided.

    Returns:
        String containing top 5 search results.
    """

    executor = ThreadPoolExecutor(max_workers=2)
    get_result_call = executor.submit(
        get_result,
        search_text,
    )

    insert_search_text_call = executor.submit(
        insert_search_text,
        search_text,
        user_id,
    )

    wait([get_result_call, insert_search_text_call])
    executor.shutdown(wait=True)
    insert_search_text_call.result()
    return get_result_call.result()


def get_result(search_text):
    """Fetches results from google custom search API.

    Args:
        search_text: Search text provided.

    Returns:
        String containing top 5 search results.
    """

    response = requests.get(
        url=GOOGLE_CUSTOM_SEARCH_URI,
        params={
            "key": GOOGLE_API_KEY,
            "cx": SEARCH_ENGINE_ID,
            "q": search_text,
            "num": 5,
        },
    )
    response_json = response.json()
    blocks = []
    for item in response_json["items"]:
        blocks.append(
            "**"
            + str(item["title"])
            + "**"
            + "\n"
            + item["snippet"]
            + item["link"]
            + "\n\n"
        )
    return blocks


def insert_search_text(search_text, user_id):
    """Stores searched text in database.

    Args:
        search_text: Search text provided.
        user_id: Id of discord user.
    """

    doc = list(
        db["SearchHistory"].find(
            {"userId": user_id, "searchTerm": search_text},
        )
    )
    if not doc:
        db["SearchHistory"].insert_one(
            {"userId": user_id, "searchTerm": search_text}
        )


def get_search_history(search_text, user_id):
    """Fetches search history of a user.

    Args:
        search_text: Search text provided.
        user_id: Id of discord user.

    Returns:
        Previous matched search terms.
    """

    docs = list(
        db["SearchHistory"].find(
            {
                "userId": user_id,
                "searchTerm": {"$regex": search_text, "$options": "i"},
            }
        )
    )

    blocks = ""
    for doc in docs:
        blocks += str(doc["searchTerm"]) + "\n"

    return blocks
