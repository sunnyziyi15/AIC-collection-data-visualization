import pandas as pd
import streamlit as st
import plotly.express as px

st.title("The Art Institute of Chicago Collection Visualization")
st.markdown("Welcome to **AIC Collection Visualization** – an interactive dashboard showcasing insights from the Art Institute of Chicago's collection.")

st.image("Sky_Above_Clouds_IV.png", caption="Sky_Above_Clouds_IV", use_column_width=True)

#read data
df = pd.read_csv("artic_artworks.csv")
print(df["artwork_type_title"].unique())

#treemap data cleaning
us_keywords = [
    "swanson street, 113",
    "united states",
    "philadelphia",
    "chicago",
    "boston",
    "new york city",
    "providence",
    "new york",
    "monterey",
    "hartford",
    "barnstable",
    "syracuse",
    "san francisco",
    "brooklyn",
    "wichita",
    "los angeles",
    "park ridge",
    "baltimore",
    "maine",
    "manhattan",
    "wilmington",
    "bloomfield hills",
    "harper woods",
    "lubbock",
    "arizona",
    "michigan avenue, 435 north",
    "kenilworth",
    "highland park",
    "ellison bay",
    "south bend",
    "minneapolis",
    "woodland avenue",
    "maxwell street, 1006-1010",
    "dundee avenue, 647 south",
    "winnetka",
    "morgantown",
    "lasalle street, 102-116 south",
    "davenport",
    "lake shore drive, 2300 south",
    "north barrington",
    "tulsa",
    "jacksonville",
    "massachusetts",
    "cook county",
    "cleveland",
    "seattle",
    "glenview",
    "berkeley",
    "madison",
    "glencoe",
    "dwight",
    "elmhurst",
    "michigan avenue, 744 north",
    "o'hare international airport",
    "michigan avenue, 20 north",
    "elkhart",
    "illinois",
    "barrington",
    "coonley road, 336",
    "michigan avenue at 24th street",
    "bend",
    "navy pier",
    "woodlawn avenue, 5622 south",
    "12th place, 554 west",
    "grant park",
    "pittsburgh",
    "lincoln park zoo",
    "kansas city",
    "michigan avenue, 360 north",
    "cityfront plaza, 450 north",
    "randolph street, 100 west",
    "chippewa falls",
    "burnham park",
    "florida",
    "john f. kennedy international airport",
    "milwaukee",
    "connecticut",
    "river forest",
    "michigan",
    "quincy",
    "art institute of chicago",
    "midwest city",
    "kenosha",
    "oak brook",
    "las vegas",
    "luxor",
    "iowa",
    "kohler",
    "des moines",
    "downers grove",
    "detroit",
    "champaign",
    "jackson hole",
    "fort wayne",
    "wheaton",
    "la crosse",
    "sleepy hollow",
    "state street, 1255 north (apartment building)",
    "madison street, 29 east",
    "lasalle street, 209 south",
    "dixon",
    "idaho",
    "northbrook",
    "walworth",
    "ridge road, 722",
    "dearborn street, 30-32 north",
    "mcdonalds plaza, 1",
    "rockford",
    "astor street, 1350 north (apartment building)",
    "california",
    "meacham road, 645 south",
    "evanston",
    "tacoma",
    "south shore park",
    "winona",
    "new haven",
    "sioux falls",
    "sheridan road, 5555 north",
    "peoria",
    "lisle",
    "libertyville",
    "miami beach",
    "manistique",
    "oshkosh",
    "michigan avenue",
    "skokie",
    "brown deer",
    "mount prospect",
    "south park botanical garden",
    "world's columbian exposition",
    "prescott",
    "lake minnetonka",
    "adirondack mountains",
    "lincoln park zoo large mammal complex",
    "van buren street, 140 west",
    "oak park",
    "district of columbia",
    "colorado springs",
    "green bay road, 1724 south",
    "grand rapids",
    "wisconsin",
    "randolph street, 62 east",
    "pomona",
    "bryn mawr avenue, 8750 west",
    "youngstown",
    "81st street at cottage grove avenue",
    "lake bluff",
    "new orleans",
    "stony brook",
    "atlantic city",
    "new jersey",
    "hampton falls",
    "ventura",
    "guam island",
    "delaware",
    "roxbury",
    "riverside",
    "indiana",
    "pennsylvania",
    "atlanta",
    "ohio",
    "georgia",
    "chicago heights",
    "kentucky",
    "missouri",
    "rhode island",
    "southern illinois",
    "greensburg",
    "new hampshire",
    "kansas",
    "oneida county",
    "bucks county",
    "maryland",
    "vermont",
    "new mexico",
    "north carolina",
    "san juan", 
    "oregon",
    "columbus",
    "midway airport",
    "cedar rapids",
    "brunswick",
    "muncie",
    "glens falls",
    "middlebury",
    "minnesota",
    "northwest coast",
    "tennessee",
    "sarasota",
    "ocean springs",
    "topeka",
    "phoenix",
    "san diego",
    "northern illinois",
    "dayton",
    "aurora",
    "west palm beach",
    "woodstock",
    "denver",
    "houston",
    "taunton",
    "flossmoor",
    "greenwich",
    "saint louis",
    "pasadena",
    "albany county",
    "new england"
]

#define color for treemap
candy_colors = [
    "#FFC4C6","#FFECD8","#EBC5E3","#DCEAF6","#DCEAF6","#DFEAF6","#FFFEFA","#E4EEC7","#FBF9D7","#FFCCE7","#FFDDF4","#B8E6B3","#F7F1AB","#9EDBA2","#DCD6FF","#DEFFEF","#F8E9E1","#EBC5E3","#F4C8B9","#8CBDBD","#F3DFAD","#F5F8F3", "#FFDCC9"
]


def map_region(place):

    if pd.isnull(place):
        return "non-US"
    place_lower = place.lower()
    if any(keyword in place_lower for keyword in us_keywords):
        return "US"
    else:
        return "non-US"

df["region"] = df["place_of_origin"].apply(map_region)


def map_period(year):

    if pd.isnull(year):
        return "Unknown"
    year_val = float(year)
    if year_val >= 1975:
        return "Contemporary Art"
    elif 1860 <= year_val < 1975:
        return "Modern Art"
    else:
        return "Pre-modern Art"

df["period"] = df["date_end"].apply(map_period)



df_agg = df.groupby(
    ["region", "period", "artwork_type_title"], 
    as_index=False
).agg({"id": "count"})
df_agg.rename(columns={"id": "count"}, inplace=True)


df_agg["artwork_type_title"] = df_agg["artwork_type_title"].fillna("Unknown Type")



#treemap title
st.subheader("Hierarchical view of AIC collection")

#plot treemap
fig = px.treemap(
    df_agg,
    path=["region", "period", "artwork_type_title"],
    values="count",
    color="artwork_type_title",
    # color_discrete_sequence=px.colors.qualitative.Dark24,
    color_discrete_sequence=candy_colors,
    hover_data=["count"]
)


fig.update_layout(
    width=1000,
    height=800
)
st.plotly_chart(fig, use_container_width=True)




#line chart data cleaning
df["date_end"] = pd.to_numeric(df["date_end"], errors="coerce")
df = df.dropna(subset=["date_end"])
df_contemporary = df[(df["date_end"] >= 1975) & (df["date_end"] <= 2025)]
df_contemporary["date_end"] = df_contemporary["date_end"].astype(int)
counts_by_media = df_contemporary.groupby("artwork_type_title")["id"].count()
valid_media = counts_by_media[counts_by_media > 0].index.tolist()
valid_media = sorted(m.strip() for m in valid_media if isinstance(m, str) and m.strip() != "")

# title
st.subheader("Line Chart by Year and Media in Contemporary Art Period")

# selection
selected_media = st.multiselect(
    "Select Media",
    valid_media,
    default=valid_media
)

filtered_df = df_contemporary[df_contemporary["artwork_type_title"].isin(selected_media)]

counts_by_year_media = (
    filtered_df
    .groupby(["date_end", "artwork_type_title"])["id"]
    .count()
    .reset_index(name="collection_count")
    .sort_values("date_end")
)

# plot
fig = px.line(
    counts_by_year_media,
    x="date_end",
    y="collection_count",
    color="artwork_type_title",
    labels={
        "date_end": "Year",
        "artwork_type_title": "Media",
        "collection_count": "Count of Artworks"
    },
    title="Number of Artworks in AIC by Year (1975–2025)",
)

# only int on x-aixs
fig.update_xaxes(dtick=1)
st.plotly_chart(fig, use_container_width=True)

# source
st.markdown("Source: Art Institute of Chicago API [https://api.artic.edu/](https://api.artic.edu/)")
