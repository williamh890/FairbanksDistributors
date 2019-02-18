
export const routes = [
    {
        "storeName": "West Freds",
        "rsr": ["Nick T.", "Bill", "Angus", "Aaron"]
    },
    {
        "storeName": "S2754",
        "rsr": ["Nick T.", "Bill", "Angus"]
    },
    {
        "storeName": "S1821",
        "rsr": ["Nick T.", "Bill", "Angus"]
    },
    {
        "storeName": "East Freds",
        "rsr": ["Don", "Carrie", "Nick F."]
    },
    {
        "storeName": "S3410",
        "rsr": ["Don", "Carrie", "Nick F."]
    },
    {
        "storeName": "Walmart",
        "rsr": ["Terry C.", "Ryan", "Shawn", "Duane", "Aaron"]
    },
    {
        "storeName": "Costco",
        "rsr": "Shawn"
    },
    {
        "storeName": "Wainwright Shoppete",
        "rsr": "Terry C."
    },
    {
        "storeName": "Wainwright Commissary",
        "rsr": ["Terry C.", "Ryan"]
    }
];

export const routeServiceReps = Array.from( new Set(routes
  .map(item => item.rsr)));

export const storeName = Array.from( new Set(routes
  .map(item => item.storeName)));
