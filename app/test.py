from  .models import Blog
blog_instance = Blog.objects.create(
    title="Sample Blog Post 1",
    body="This is the body of the sample blog post 1."

)