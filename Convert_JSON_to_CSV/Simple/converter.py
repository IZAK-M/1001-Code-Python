import json

if __name__ == "__main__":
    try:
        with open("input.json", "r") as f:
            data = json.loads(f.read())

        output = ",".join([*data[0]])
        for obj in data:
            output += f'\n{obj["id"]}, {obj["nom"]}, {obj["metier"]}, {obj["experience"]}, {obj["competences"]}'

        with open("output.csv", "w") as f:
            f.write(output)
            print("✅ Conversion terminée avec succès")
    except Exception as ex:
        print(f"Erreur: {str(ex)}")
