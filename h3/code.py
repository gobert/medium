def lat_lng_to_h3():
    import h3

    h3_key = h3.geo_to_h3(lat=48.853, lng=2.348, resolution=8)
    print(h3_key)
    # returns
    "881fb46625fffff"


def h3_to_geo_boundary():
    import h3

    hexagon_tuple2d = h3.h3_to_geo_boundary(h="881f89b0b9fffff")
    print(hexagon_tuple2d)
    # returns
    (
        (48.00281717023803, 12.99819043295637),
        (47.998312559890245, 12.996138504924922),
        (47.99513376112209, 13.001125772015417),
        (47.996459408079176, 13.008165144025583),
        (48.00096400408189, 13.010217832868259),
        (48.00414296749273, 13.005230388946893),
    )


def h3_to_geo_boundary_geojson():
    import h3

    # 1. convertit un tuples de tuples en tableau 3d (tableau de tableau de
    # tableau)
    coordinates_geojson = [
        list(
            map(
                lambda h: list(h),
                h3.h3_to_geo_boundary(h="881f89b0b9fffff", geo_json=True),
            )
        )
    ]
    # 2. formatte en geojson
    hexagon_geojson = {
        "type": "Polygon",
        "coordinates": coordinates_geojson,
    }
    # 3. afficht les resulats
    print(hexagon_geojson)
    print("")
    # returns
    {
        "type": "Polygon",
        "coordinates": [
            [
                [12.99819043295637, 48.00281717023803],
                [12.996138504924922, 47.998312559890245],
                [13.001125772015417, 47.99513376112209],
                [13.008165144025583, 47.996459408079176],
                [13.010217832868259, 48.00096400408189],
                [13.005230388946893, 48.00414296749273],
                [12.99819043295637, 48.00281717023803],
            ]
        ],
    }


def polyfill():
    import h3

    # 1. Definit le polygon à remplir en geojson
    #
    # En geojson:
    # -les polygons sont décris dans le sens inverse des aiguilles d'une montre
    # - le premier point doit-être répété à la fin.
    # - les points sont décris comme un tableau en 3 dimensions
    #  [[[latitude, longitude]]]
    polygon_geojson = {
        "type": "Polygon",
        "coordinates": [
            [
                [2.25, 48.82],  # point0: sud ouest de Paris
                [2.40, 48.82],  # point1: sud est de Paris
                [2.40, 48.89],  # point2: nord est de Paris
                [2.25, 48.89],  # point3: nord ouest de Paris
                [2.25, 48.82],  # point4: sud ouest de Paris
            ]
        ],
    }
    # 2. Appelle polyfill
    geocodes = h3.polyfill(
        geojson=polygon_geojson, res=8, geo_json_conformant=True
    )
    # 3. Affiche les resultat
    print(set(list(geocodes)[0:10]))
    print("")
    # returns
    {
        "881fb46755fffff",
        "881fb475a7fffff",
        "881fb46639fffff",
        "881fb46739fffff",
        "881fb46601fffff",
        "881fb475abfffff",
        "881fb46441fffff",
        "881fb4660dfffff",
        "881fb4674dfffff",
        "881fb4666dfffff",
    }


if __name__ == "__main__":
    print("Convertir une paire latitude/longitude vers une clé H3")
    lat_lng_to_h3()
    print("")

    print("Convertir une clé H3 vers les 6 coordonées d'un hexagon")
    h3_to_geo_boundary()
    print("")

    print("Convertir une clé H3 vers les 6 coordonées d'un hexagon en geojson")
    h3_to_geo_boundary_geojson()
    print("")

    print("Trouver tous les hexagons dans un polygon")
    polyfill()
