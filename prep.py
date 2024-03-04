import tensorflow_transform as tft


def preprocessing_fn(inputs):
    
    outputs = {}

    for categorical_feature in ['Wilderness_Area', 'Soil_Type']:
        outputs[categorical_feature] = tft.compute_and_apply_vocabulary(inputs[categorical_feature])
    
    for numeric_feature in ['Elevation', 'Slope', 'Horizontal_Distance_To_Hydrology', 'Vertical_Distance_To_Hydrology', 'Horizontal_Distance_To_Roadways', 'Hillshade_9am', 'Hillshade_Noon', 'Horizontal_Distance_To_Fire_Points']:
        outputs[numeric_feature] = tft.scale_to_z_score(inputs[numeric_feature])
    
    outputs['Cover_Type'] = tft.bucketize(inputs['Cover_Type'], num_buckets=7)
    
    return outputs
