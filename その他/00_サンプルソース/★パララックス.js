// 写真ボックスにパララックス効果を適用
window.addEventListener("scroll", () => {
  const scrollY = window.scrollY;

  document.querySelectorAll(".photo-box").forEach((box) => {
    const speed = parseFloat(box.dataset.speed) || 0.5;
    // スクロール方向と逆に動かす（マイナス）
    box.style.transform = `translateY(${-scrollY * speed}px)`;
  });
});
