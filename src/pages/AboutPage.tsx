export function AboutPage() {
  return (
    <section className="about-page">
      <h1>About</h1>
      <p>
        Engineering Calculator is a student-built educational project. The goal is to organize
        useful math, physics, and engineering formulas in one searchable place, so studying and
        homework don't mean digging through a stack of different textbooks and websites.
      </p>
      <p>
        Everything here — the formula database, the search, and the calculators — is built and
        maintained by one student, as a learning project in React, TypeScript, and everyday
        software engineering.
      </p>
      <p className="disclaimer">
        <strong>Educational tool disclaimer:</strong> This site is for learning and studying. Formula
        results should be independently verified before being used for professional or
        safety-critical engineering work.
      </p>
    </section>
  );
}
