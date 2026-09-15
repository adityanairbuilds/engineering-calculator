import type { Route } from '../hooks/useRouter';

const LINKS: { route: Route; label: string }[] = [
  { route: 'home', label: 'Home' },
  { route: 'calculator', label: 'Calculator' },
  { route: 'library', label: 'Formula Library' },
  { route: 'about', label: 'About' },
];

export function NavBar({ route, navigate }: { route: Route; navigate: (r: Route) => void }) {
  return (
    <header className="site-header">
      <nav className="site-nav">
        <button type="button" className="brand" onClick={() => navigate('home')}>
          Engineering Calculator
        </button>
        <ul className="links">
          {LINKS.map((link) => (
            <li key={link.route}>
              <button
                type="button"
                aria-current={route === link.route ? 'page' : undefined}
                onClick={() => navigate(link.route)}
              >
                {link.label}
              </button>
            </li>
          ))}
        </ul>
      </nav>
    </header>
  );
}
