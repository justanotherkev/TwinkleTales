def individual_serial(storygen) -> dict:
        return {
        "id": str(storygen["_id"]),
        "audio_url" : storygen.get("audio_url", ""),  # Use .get() to safely access the key
        "description": storygen.get("description", "")  # Use .get() to safely access the key
    }


def list_serial (storygens) -> list:
    return[individual_serial(storygen) for storygen in storygens]
 