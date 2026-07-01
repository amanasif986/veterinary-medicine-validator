# =======================================================
# BASE PET CLASS (INHERITED BY ALL PET TYPES)
# =======================================================

class PetBase:
    name = ""
    species = []
    weight_classes = ["Small", "Medium", "Large"]

    medicines = {}   # To be overridden
    compounds = {}   # To be overridden

    # Unified weight-based concentration adjustment
    @staticmethod
    def adjust_concentration(min_val, max_val, weight_class):
        if weight_class == "Small":
            return min_val
        elif weight_class == "Medium":
            return (min_val + max_val) // 2
        elif weight_class == "Large":
            return max_val
        return min_val


# =======================================================
# PET SUBCLASSES (INHERITING FROM PetBase)
# =======================================================

class Dog(PetBase):
    name = "Dog"
    species = ["Labrador", "Bulldog", "German Shepherd"]

    medicines = {
        "DogPainRelief": ["CanineAmoxicillin", "CanineIbuprofen"],
        "DogColdTreatment": ["CanineVitaminC", "CanineAntihistamine"],
        "DogJointSupport": ["CanineGlucosamine", "CanineChondroitin"],
        "DogDigestiveAid": ["CanineProbiotic", "CanineFiber"],
        "DogSkinCare": ["CanineOmega3", "CanineZinc"],
    }

    compounds = {
        "CanineAmoxicillin": (5, 12),
        "CanineIbuprofen": (1, 3),
        "CanineVitaminC": (2, 6),
        "CanineAntihistamine": (1, 2),
        "CanineGlucosamine": (3, 7),
        "CanineChondroitin": (2, 5),
        "CanineProbiotic": (1, 3),
        "CanineFiber": (2, 4),
        "CanineOmega3": (1, 3),
        "CanineZinc": (1, 2),
    }


class Cat(PetBase):
    name = "Cat"
    species = ["Persian", "Siamese", "Maine Coon"]

    medicines = {
        "CatAntiInflammatory": ["FelineCefalexin", "FelinePrednisolone"],
        "CatColdRelief": ["FelineVitaminC", "FelineAntihistamine"],
        "CatJointSupport": ["FelineGlucosamine", "FelineChondroitin"],
        "CatDigestiveAid": ["FelineProbiotic", "FelineFiber"],
        "CatSkinCare": ["FelineOmega3", "FelineZinc"],
    }

    compounds = {
        "FelineCefalexin": (4, 10),
        "FelinePrednisolone": (1, 5),
        "FelineVitaminC": (2, 6),
        "FelineAntihistamine": (1, 2),
        "FelineGlucosamine": (3, 7),
        "FelineChondroitin": (2, 5),
        "FelineProbiotic": (1, 3),
        "FelineFiber": (2, 4),
        "FelineOmega3": (1, 3),
        "FelineZinc": (1, 2),
    }


class Rabbit(PetBase):
    name = "Rabbit"
    species = ["Rex", "Dutch", "Lionhead"]

    medicines = {
        "RabbitAntibioticMix": ["RabbitEnrofloxacin", "RabbitVitaminMix"],
        "RabbitColdTreatment": ["RabbitVitaminC", "RabbitAntihistamine"],
        "RabbitJointSupport": ["RabbitGlucosamine", "RabbitChondroitin"],
        "RabbitDigestiveAid": ["RabbitProbiotic", "RabbitFiber"],
        "RabbitSkinCare": ["RabbitOmega3", "RabbitZinc"],
    }

    compounds = {
        "RabbitEnrofloxacin": (2, 6),
        "RabbitVitaminMix": (1, 4),
        "RabbitVitaminC": (2, 6),
        "RabbitAntihistamine": (1, 2),
        "RabbitGlucosamine": (3, 7),
        "RabbitChondroitin": (2, 5),
        "RabbitProbiotic": (1, 3),
        "RabbitFiber": (2, 4),
        "RabbitOmega3": (1, 3),
        "RabbitZinc": (1, 2),
    }


class Parrot(PetBase):
    name = "Parrot"
    species = ["Macaw", "Cockatiel", "African Grey"]

    medicines = {
        "ParrotBoneSupport": ["AvianCalciumBoost", "AvianDoxycycline"],
        "ParrotColdTreatment": ["AvianVitaminC", "AvianAntihistamine"],
        "ParrotFeatherHealth": ["AvianOmega3", "AvianZinc"],
        "ParrotDigestiveAid": ["AvianProbiotic", "AvianFiber"],
        "ParrotVisionSupport": ["AvianVitaminA", "AvianLutein"],
    }

    compounds = {
        "AvianCalciumBoost": (2, 5),
        "AvianDoxycycline": (4, 8),
        "AvianVitaminC": (2, 6),
        "AvianAntihistamine": (1, 2),
        "AvianOmega3": (1, 3),
        "AvianZinc": (1, 2),
        "AvianProbiotic": (1, 3),
        "AvianFiber": (2, 4),
        "AvianVitaminA": (1, 4),
        "AvianLutein": (1, 3),
    }


class Hamster(PetBase):
    name = "Hamster"
    species = ["Syrian", "Dwarf", "Chinese"]

    medicines = {
        "HamsterDigestiveSupport": ["RodentProbiotic", "RodentElectrolyteMix"],
        "HamsterColdTreatment": ["RodentVitaminC", "RodentAntihistamine"],
        "HamsterJointSupport": ["RodentGlucosamine", "RodentChondroitin"],
        "HamsterSkinCare": ["RodentOmega3", "RodentZinc"],
        "HamsterEnergyBoost": ["RodentCaffeine", "RodentVitaminB"],
    }

    compounds = {
        "RodentProbiotic": (1, 3),
        "RodentElectrolyteMix": (1, 2),
        "RodentVitaminC": (2, 6),
        "RodentAntihistamine": (1, 2),
        "RodentGlucosamine": (3, 7),
        "RodentChondroitin": (2, 5),
        "RodentOmega3": (1, 3),
        "RodentZinc": (1, 2),
        "RodentCaffeine": (1, 2),
        "RodentVitaminB": (1, 3),
    }


# Map menu numbers to classes
PETS = {
    "1": Dog,
    "2": Cat,
    "3": Rabbit,
    "4": Parrot,
    "5": Hamster,
}


# =======================================================
# INTERACTION / SELECTION FUNCTIONS
# =======================================================

def choose_pet():
    print("\nChoose a pet:")
    for k, v in PETS.items():
        print(f"{k}. {v.name}")
    return PETS.get(input("Enter pet (1-5): ").strip(), Rabbit)()

 
def choose_species(pet):
    print("\nChoose species:")
    for i, sp in enumerate(pet.species, 1):
        print(f"{i}. {sp}")
    ch = input("Enter choice (or Enter for first): ").strip()
    return pet.species[int(ch) - 1] if ch.isdigit() and 1 <= int(ch) <= len(pet.species) else pet.species[0]


def choose_weight(pet):
    print("\nChoose weight class:")
    for i, w in enumerate(pet.weight_classes, 1):
        print(f"{i}. {w}")
    ch = input("Enter choice (or Enter for Medium): ").strip()
    return pet.weight_classes[int(ch) - 1] if ch.isdigit() else "Medium"


def choose_medicine(pet):
    print(f"\nMedicines for {pet.name}:")
    meds = list(pet.medicines.keys())
    for i, m in enumerate(meds, 1):
        print(f"{i}. {m}")
    ch = input("Choose medicine (or Enter for first): ").strip()
    return meds[int(ch) - 1] if ch.isdigit() else meds[0]


# =======================================================
# DANGEROUS MIXTURE LOGIC
# =======================================================

DANGEROUS = {
    ("CanineIbuprofen", "FelineCefalexin"),
    ("AvianCalciumBoost", "AvianDoxycycline"),
    ("RodentElectrolyteMix", "RabbitEnrofloxacin"),
}

SAFE_ALTERNATIVES = {
    "CanineIbuprofen": "CanineAmoxicillin",
    "FelineCefalexin": "FelinePrednisolone",
    "AvianCalciumBoost": "RabbitVitaminMix",
    "AvianDoxycycline": "RabbitVitaminMix",
    "RodentElectrolyteMix": "RodentProbiotic",
    "RabbitEnrofloxacin": "RabbitVitaminMix",
}

def is_dangerous(a, b):
    return (a, b) in DANGEROUS or (b, a) in DANGEROUS


# =======================================================
# COMPOUND + CONCENTRATION INPUT
# =======================================================

def choose_compound(pet, used):
    options = [c for c in pet.compounds if c not in used]

    print("\nAvailable compounds:")
    for i, c in enumerate(options, 1):
        mn, mx = pet.compounds[c]
        print(f"{i}. {c} ({mn}-{mx}%)")

    ch = input("Choose compound (or Enter for first): ").strip()
    return options[int(ch) - 1] if ch.isdigit() else options[0]


def get_concentration(pet, comp, weight):
    mn, mx = pet.compounds[comp]
    recommend = pet.adjust_concentration(mn, mx, weight)

    print(f"\nEnter concentration for {comp}")
    print(f"Safe: {mn}-{mx}% | Recommended ({weight}): {recommend}%")

    while True:
        try:
            val = int(input("Enter %: ").strip())
            if mn <= val <= mx:
                return val
            print(f"❌ Must be between {mn}-{mx}%.")
        except:
            print("Invalid input. Enter a number.")


# =======================================================
# VALIDATION
# =======================================================

def validate(pet, medicine, mixture):
    required = pet.medicines[medicine]
    user_comps = [c for c, _ in mixture]

    print("\n-------------------------------")
    print(f"Validating mixture for {medicine}")
    print("-------------------------------")

    if set(required) != set(user_comps):
        print("❌ ERROR: Incorrect compounds!")
        print("Required:", required)
        print("Given:", user_comps)
        return

    # dangerous?
    a, aC = mixture[0]
    b, bC = mixture[1]

    if is_dangerous(a, b):
        print(f"⚠️ DANGEROUS: {a} + {b}")
        print("Suggested alternatives:")
        print(f" - {a}: {SAFE_ALTERNATIVES.get(a)}")
        print(f" - {b}: {SAFE_ALTERNATIVES.get(b)}")
        return

    # range check
    for comp, val in mixture:
        mn, mx = pet.compounds[comp]
        if not (mn <= val <= mx):
            print(f"❌ {comp} concentration out of range ({mn}-{mx}%).")
            return

    print("✅ Mixture is SAFE!")


# =======================================================
# MAIN PROGRAM
# =======================================================

def main():
    print("\n=== Veterinary Medicine Generator ===")

    pet = choose_pet()
    species = choose_species(pet)
    weight = choose_weight(pet)

    print(f"\nSelected: {pet.name} ({species}, {weight})")

    medicine = choose_medicine(pet)
    mixture = []

    for _ in range(2):
        comp = choose_compound(pet, used=[c for c, _ in mixture])
        conc = get_concentration(pet, comp, weight)
        mixture.append((comp, conc))

    validate(pet, medicine, mixture)


if __name__ == "__main__":
    main()
