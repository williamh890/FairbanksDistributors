
export const routes = [
    {
        "store": "West Freds",
        "rsr": ["Nick T.", "Bill", "Angus", "Aaron"]
    },
    {
        "store": "S2754",
        "rsr": ["Nick T.", "Bill", "Angus"]
    },
    {
        "store": "S1821",
        "rsr": ["Nick T.", "Bill", "Angus"]
    },
    {
        "store": "East Freds",
        "rsr": ["Don", "Carrie", "Nick F."]
    },
    {
        "store": "S3410",
        "rsr": ["Don", "Carrie", "Nick F."]
    },
    {
        "store": "Walmart",
        "rsr": ["Terry C.", "Ryan", "Shawn", "Duane", "Aaron"]
    },
    {
        "store": "Costco",
        "rsr": "Shawn"
    },
    {
        "store": "Wainwright Shoppete",
        "rsr": "Terry C."
    },
    {
        "store": "Wainwright Commissary",
        "rsr": ["Terry C.", "Ryan"]
    }
];

export const routeServiceReps = Array.from( new Set(routes
  .map(item => item.rsr)));
