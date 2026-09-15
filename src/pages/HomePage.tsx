import type { Route } from '../hooks/useRouter';
import { categoryTree } from '../data/formulas';

export function HomePage({ navigate }: { navigate: (r: Route) => void }) {
  return (
    <section className="home">
      <h1>Engineering Calculator</h1>
      <p>
        Engineering Calculator is a student project that puts hundreds of useful math, physics, and
        engineering formulas in one place. It's designed to help with homework and studying, and
        hopefully someday be useful in classrooms if teachers approve it.
      </p>
      <div className="home-actions">
        <button type="button" className="btn" onClick={() => navigate('calculator')}>
          Open the Calculator
        </button>
        <button type="button" className="btn btn-outline" onClick={() => navigate('library')}>
          Browse the Formula Library
        </button>
      </div>

      <h2 className="home-subjects-heading">Subjects covered</h2>
      <ul className="home-subjects">
        {categoryTree.map((c) => (
          <li key={c.name}>
            <strong>{c.name}:</strong> {c.subcategories.join(', ')}
          </li>
        ))}
      </ul>
    </section>
  );
}
