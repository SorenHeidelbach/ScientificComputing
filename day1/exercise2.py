
# %% Exercise 2: sorting


def sort_stars(stars, key):
    key_to_index = {
        "distance":1,
        "brightness":2,
        "lumen":3
    }
    return sorted(stars, key = lambda x: x[key_to_index[key]])

if __name__ == "__main__":
    with open("stars.list") as f:
        exec(f.read())
    sort_stars(data, "lumen")


