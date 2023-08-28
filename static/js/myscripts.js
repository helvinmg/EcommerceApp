console.log("test")
function addone()
{
    q=parseInt(document.getElementById('quantity').textContent)
    document.getElementById('quantity').textContent=q+1
}
function removeone()
{
    q=parseInt(document.getElementById('quantity').textContent)
    document.getElementById('quantity').textContent=q-1
}