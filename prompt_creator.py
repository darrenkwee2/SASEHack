import os
import openai

# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = ""


def main():
    user_input = input("How are you feeling today? ")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You will be provided with a description of how a user is feeling. Your "
                                          "task is to assign values from -3 to 3 (-3 be the most negative, "
                                          "3 being the most positive) for the following elements: "
                                          "How much physical energy the user has, "
                                          "how much social energy the user has, "
                                          "how much nervous energy the user has."
                                          "Also, please provide a brief description justifying your choices."},
            {"role": "user", "content": generate_prompt(user_input)}
        ],
        # prompt=generate_prompt(user_input),
        temperature=1,
        max_tokens=1024
    )

    for i in range(len(response.choices)):
        print(response.choices[i].message.content)


def generate_prompt(feeling):
    return ("""You will be provided with a description of how a user is feeling. 
    Your task is to assign values from -3 to 3 (-3 be the most negative, 3 being the most positive)
     for the following elements: 
     How much physical energy the user has, 
     how much social energy the user has, 
     how much nervous energy the user has. """
            .format(feeling.capitalize()))


if __name__ == "__main__":
    main()
