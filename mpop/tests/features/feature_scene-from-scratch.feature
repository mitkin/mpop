@wip
Feature: Make scene from scratch

    Scientific user Joe has some data sitting in his hardrive.
    It's a spatial data, so he has at least three arrays:
    Data, Latitudes and Longitudes. He also knows approximately when this data was sampled,
    meaining he's got a single time stamp. It could be a NWP field.
    He heard PyTroll is great at handling spatial data, so he gives it a try.
    Joe is lazy as most (programmers) so he wants to provide minimum information
    to the library. He has no configs. Resampling the data to a grid would be
    quite satisfying. So he just wants to see, whether it's possible to
    provide information piece by piece to the point there would be enough information
    to resample his data

    Scenario: User can initialize, populate and resample Scene step by step
        Given data, longitudes and latitudes are available
        Given area definition is available
        Given timestamp is available
        When user loads the data, coordinates, timestamp and area definition
        Then scene is resampleable
