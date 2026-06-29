from collections import deque


def extract_nft_names(nft_collection):
    Names: list[str] = []
    for nft in nft_collection:
        Names.append(nft.get("name"))
    return Names

# Example usage:
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

#print(extract_nft_names(nft_collection))
#print(extract_nft_names(nft_collection_2))
#print(extract_nft_names(nft_collection_3))


# Q2

def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names.append(nft["name"])
    return nft_names

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2}
]

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

nft_collection_3 = []

#print(extract_nft_names(nft_collection))
#print(extract_nft_names(nft_collection_2))
#print(extract_nft_names(nft_collection_3))

def identify_popular_creators(nft_collection):
    NFTFreq: dict[str, int] = {}
    for nft in nft_collection:
        if nft.get("creator") not in NFTFreq:
            NFTFreq[nft.get("creator")] = 1
        else:
            NFTFreq[nft.get("creator")] +=1
    popular: list[str] = []
    for creator, created in NFTFreq.items():
        if created > 1:
            popular.append(creator)
    return popular


nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

#print(identify_popular_creators(nft_collection))
#print(identify_popular_creators(nft_collection_2))
#print(identify_popular_creators(nft_collection_3))


def average_nft_value(nft_collection):
    avg: float = 0
    if len(nft_collection) == 0:
        return 0
    for nft in nft_collection:
        avg += nft.get("value")
    avg = avg / len(nft_collection)
    return avg


nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]
#print(average_nft_value(nft_collection))

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
    {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
]
#print(average_nft_value(nft_collection_2))

nft_collection_3 = []
#print(average_nft_value(nft_collection_3))


def search_nft_by_tag(nft_collections, tag):
    target: list[str] = []
    for i in range(len(nft_collections)):
        for j in range(len(nft_collections[i])):
            if tag in nft_collections[i][j].get("tags"):
                target.append(nft_collections[i][j].get("name"))
    return target


nft_collections = [
    [
        {"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
        {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}
    ],
    [
        {"name": "Urban Jungle", "tags": ["urban", "landscape"]},
        {"name": "City Lights", "tags": ["modern", "landscape"]}
    ]
]

nft_collections_2 = [
    [
        {"name": "Golden Hour", "tags": ["sunset", "landscape"]},
        {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}
    ],
    [
        {"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}
    ]
]

nft_collections_3 = [
    [
        {"name": "The Last Piece", "tags": ["finale", "abstract"]}
    ],
    [
        {"name": "Ocean Waves", "tags": ["seascape", "calm"]},
        {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}
    ]
]

#print(search_nft_by_tag(nft_collections, "landscape"))
#print(search_nft_by_tag(nft_collections_2, "sunset"))
#print(search_nft_by_tag(nft_collections_3, "modern"))


def process_nft_queue(nft_queue):
    order: list[str] = []
    queue: deque[str] = deque()

    for nft in nft_queue:
        queue.append(nft.get("name"))

    for nft in queue:
        order.append(nft)

    return order

nft_queue = [
    {"name": "Abstract Horizon", "processing_time": 2},
    {"name": "Pixel Dreams", "processing_time": 3},
    {"name": "Urban Jungle", "processing_time": 1}
]
#print(process_nft_queue(nft_queue))

nft_queue_2 = [
    {"name": "Golden Hour", "processing_time": 4},
    {"name": "Sunset Serenade", "processing_time": 2},
    {"name": "Ocean Waves", "processing_time": 3}
]
#print(process_nft_queue(nft_queue_2))

nft_queue_3 = [
    {"name": "Crypto Kitty", "processing_time": 5},
    {"name": "Galactic Voyage", "processing_time": 6}
]
#print(process_nft_queue(nft_queue_3))



