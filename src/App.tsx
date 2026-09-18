import { NavBar } from './components/NavBar';
import { useRouter } from './hooks/useRouter';
import { useFormulas } from './hooks/useFormulas';
import { AboutPage } from './pages/AboutPage';
import { CalculatorPage } from './pages/CalculatorPage';
import { HomePage } from './pages/HomePage';
import { LibraryPage } from './pages/LibraryPage';
import './App.css';

function App() {
  const { route, navigate } = useRouter();
  // Fetched once here (not per-page) so switching between Home/Library/About
  // doesn't refetch or re-flash a loading state.
  const formulasState = useFormulas();

  return (
    <>
      <NavBar route={route} navigate={navigate} />
      <main>
        {route === 'calculator' && <CalculatorPage />}
        {route === 'about' && <AboutPage />}
        {(route === 'home' || route === 'library') && formulasState.status === 'loading' && (
          <p className="page-status">Loading formulas…</p>
        )}
        {(route === 'home' || route === 'library') && formulasState.status === 'error' && (
          <p className="page-status error-text">{formulasState.message}</p>
        )}
        {route === 'home' && formulasState.status === 'ok' && (
          <HomePage navigate={navigate} categoryTree={formulasState.categoryTree} />
        )}
        {route === 'library' && formulasState.status === 'ok' && (
          <LibraryPage formulas={formulasState.formulas} categoryTree={formulasState.categoryTree} />
        )}
      </main>
      <footer className="site-footer">
        <p>Educational tool — verify results independently before relying on them for real engineering work.</p>
      </footer>
    </>
  );
}

export default App;
