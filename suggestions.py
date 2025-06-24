from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_resume_tips(resume_text, job_text):
    resume_sentences = resume_text.split(".")
    job_sentences = job_text.split(".")

    resume_embeddings = model.encode(resume_sentences, convert_to_tensor=True)
    job_embeddings = model.encode(job_sentences, convert_to_tensor=True)

    similarities = util.pytorch_cos_sim(resume_embeddings, job_embeddings)

    unmatched = []
    for j, job_line in enumerate(job_sentences):
        max_sim = max(similarities[:, j])
        if max_sim < 0.4:  # Threshold for match
            unmatched.append(job_line)

    if unmatched:
        tips = "<br>".join([f"⚠️ Consider adding or improving content related to: <b>{line.strip()}</b>" for line in unmatched])
    else:
        tips = "✅ Your resume covers most of the job description requirements well."

    return tips
