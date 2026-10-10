"""Offline regression tests for catalog/registry parity and metadata roles."""

import unittest

from scripts.portfolio_governance import validate_sources


def fixture():
    catalog = {
        "schema_version": 1,
        "owner": "legacy",
        "github_owner": "canonical",
        "repositories": [
            {"repository": "sample-a", "role": "umbrella"},
            {"repository": "sample-b", "role": "standalone"},
        ],
    }
    registry = {
        "schema_version": 1,
        "owner": "legacy",
        "github_owner": "canonical",
        "domains": {"Example domain": ["sample-a"]},
        "methodologies": {"Example methodology": ["sample-b"]},
        "planned_methodological_umbrellas": ["future-method"],
    }
    return catalog, registry


class InventoryTests(unittest.TestCase):
    def test_valid_inventory_including_standalone(self):
        self.assertEqual(validate_sources(*fixture()), [])

    def test_registry_only_repository(self):
        catalog, registry = fixture()
        registry["domains"]["Example domain"].append("uncatalogued")
        self.assertTrue(any("missing from catalog" in e for e in validate_sources(catalog, registry)))

    def test_catalog_only_repository(self):
        catalog, registry = fixture()
        registry["methodologies"]["Example methodology"].clear()
        self.assertTrue(any("missing from registry" in e for e in validate_sources(catalog, registry)))

    def test_duplicate_in_group(self):
        catalog, registry = fixture()
        registry["domains"]["Example domain"].append("sample-a")
        self.assertTrue(any("duplicate repository" in e for e in validate_sources(catalog, registry)))

    def test_duplicate_catalog_record(self):
        catalog, registry = fixture()
        catalog["repositories"].append(dict(catalog["repositories"][0]))
        self.assertTrue(any("duplicate catalog" in e for e in validate_sources(catalog, registry)))

    def test_canonical_owner_drift(self):
        catalog, registry = fixture()
        registry["github_owner"] = "wrong"
        self.assertTrue(any("canonical GitHub owner" in e for e in validate_sources(catalog, registry)))

    def test_planned_overlap(self):
        catalog, registry = fixture()
        registry["planned_methodological_umbrellas"].append("sample-a")
        self.assertTrue(any("already present" in e for e in validate_sources(catalog, registry)))

    def test_unknown_role(self):
        catalog, registry = fixture()
        catalog["repositories"][0]["role"] = "fantasy"
        self.assertTrue(any("unsupported catalog role" in e for e in validate_sources(catalog, registry)))


if __name__ == "__main__":
    unittest.main()
