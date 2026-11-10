from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    lower_ing = ingredients.lower()
    if any(item in lower_ing for item in allowed):
        return "VALID"
    return "INVALID"
