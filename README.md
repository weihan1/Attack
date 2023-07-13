# Adversarial_attack
Steps:
1. Create your own dataset of essays with various topics.
2. Use api_dataset.py to generate AI-generated essays based on the same topics of your dataset.
3. Then, you can use main_training.py to train a BERT model to learn to classify whether a piece of text is written by AI or by a human.
4. Finally, run main.py and input an essay generated by ChatGPT and watch the modifications that are done.


Some results:

Original Essay generated by ChatGPT - Easily detectable by GPTZero for instance
<img width="901" alt="Screenshot 2023-07-13 at 12 07 54 AM" src="https://github.com/weihan1/Attack/assets/78453818/2114c9c8-81ac-42d4-8a9f-112808872841">


After Performing TextAttack

<img width="810" alt="Screenshot 2023-07-13 at 12 12 41 AM" src="https://github.com/weihan1/Attack/assets/78453818/d7b9f4e1-ba23-4156-95ea-066ff447db6b">

Below is the modifications that were made by the attack:

<img width="1017" alt="Screenshot 2023-07-13 at 12 13 05 AM" src="https://github.com/weihan1/Attack/assets/78453818/1d4c03fa-dc88-4093-a7b9-6b64f0706c2a">


# Note:
The adversarial attack module is using TextAttack (https://textattack.readthedocs.io/en/latest/) and the AI-generated process is using the OPENAI API (https://openai.com).
