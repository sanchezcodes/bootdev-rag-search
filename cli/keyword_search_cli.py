#!/usr/bin/env python3

import argparse
import json

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()
    
    with open('data/movies.json', 'r') as f:
        movies = json.load(f)
    
    match args.command:
        case "search":
            # print the search query here
            search(movies, args.query)
        case _:
            parser.print_help()

def search(data, search_query, max_results=5):
    """
    Search for movies by title and print up to max_results matches
    (already ordered by ascending ID as per dataset)
    
    Args:
        data (dict): Dictionary containing a 'movies' key with a list of movies
        search_query (str): Search term to look for in movie titles
        max_results (int): Maximum number of results to display
    """
    results = []

    if 'movies' not in data:
        print(f"Searching for: {search_query}")
        print("No movies found.")
        return

    for movie in data['movies']:
        if 'title' in movie and search_query.lower() in movie['title'].lower():
            results.append(movie)
            if len(results) == max_results:   # stop once we have enough
                break

    print(f"Searching for: {search_query}")
    if not results:
        print("No movies found.")
        return

    for i, movie in enumerate(results, 1):
        print(f"{i}. {movie['title']}")


if __name__ == "__main__":
    main()
