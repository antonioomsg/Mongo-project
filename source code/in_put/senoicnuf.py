#funcion para eliminar filas vacias.
def drop_null(table,subset):
    table.dropna(subset=[f"{subset}"],inplace=True)

#Funcion para transformar a Geopoints.
def transformToGeoPoint(s):
    if np.isnan(s.latitude) or np.isnan(s.longitude):
        return None
    return {
        "type":"Point",
        "coordinates":[s.longitude, s.latitude]
    }