from nltk.classify import NaiveBayesClassifier

negative_emojis = {"pouting_face": -10, "face_with_steam_from_nose": -10, "angry_face": -10, "loudly_crying_face": -9, "oncoming_fist": -8, "thumbs_down": -8, "fearful_face": -7, "anxious_face_with_sweat": -7, "disappointed_face": -7, "worried_face": -7, "sad_but_relieved_face": -6, "persevering_face": -6, "confused": -6, "frowning_face_with_open_mouth": -5, "confused_face": -5, "dizzy_face": -4, "face_screaming_in_fear": -4, "flushed_face": -4, "expressionless_face": -3, "sad_but_relieved_face": -2, "neutral_face": -1}

positive_emojis = {"red_heart": 10, "yellow_heart": 10, "blue_heart": 10, "purple_heart": 10, "green_heart": 10, "sparkling_heart": 10, "heart_with_arrow": 10, "smiling_face_with_heart": 9, "face_blowing_a_kiss": 9, "kissing_face_with_closed_eyes": 9, "star": 9, "kissing_face": 9, "smiling_face_with_smiling_eyes": 8, "laughing": 8, "satisfied": 8, "joy": 8, "grinning_face_with_smiling_eyes": 7, "grinning_face_with_big_eyes": 7, "grinning_face": 7, "beaming_face_with_smiling_eyes": 7, "ok_hand": 6, "thumbs_up": 6, "victory_hand": 6, "clapping_hands": 6, "slightly_smiling_face": 5, "grinning_face_with_sweat": 5, "smiling_face_with_halo": 5, "face_savoring_food": 5, "winking_face": 4, "smiling_face_with_sunglasses": 4, "winking_face_with_tongue": 3, "squinting_face_with_tongue": 3, "face_with_tongue": 3, "relieved_face": 2, "smiling_face": 1}


def word_feats(words):
    return dict([(word, True) for word in words])


positive_emojis = [(word_feats(key), value) for key, value in positive_emojis.items()]
negative_emojis = [(word_feats(key), value) for key, value in negative_emojis.items()]


def train():
    train_set = positive_emojis + negative_emojis
    classifier = NaiveBayesClassifier.train(train_set)
    return classifier

